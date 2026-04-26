# ProNax AI - 3D Spatial AI Engine Dockerfile
FROM rust:1.75 as builder

WORKDIR /app

# Copy Cargo files
COPY Cargo.toml Cargo.lock ./

# Create dummy main.rs to cache dependencies
RUN mkdir src && echo "fn main() {}" > src/main.rs
RUN cargo build --release && rm -rf src

# Copy source code
COPY src ./src
COPY ml ./ml
COPY kvcache ./kvcache

# Build the actual application
RUN touch src/main.rs && cargo build --release

# Runtime image
FROM debian:bookworm-slim

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    ca-certificates \
    libssl3 \
    && rm -rf /var/lib/apt/lists/*

# Create app user
RUN useradd -m -u 1000 pronax

WORKDIR /app

# Copy binary from builder
COPY --from=builder /app/target/release/pronax /usr/local/bin/

# Create model directory
RUN mkdir -p /home/pronax/.pronax/models && chown -R pronax:pronax /home/pronax

USER pronax

EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

CMD ["pronax", "ignite", "--model", "gemma-4-9b-it", "--port", "8080"]
