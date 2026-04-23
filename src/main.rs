//! ProNax AI - 3D Spatial AI Engine
//! Main CLI Entry Point with Unique Command Architecture
//!
//! Commands:
//! - forge: Download and prepare models
//! - ignite: Start inference server
//! - synthesize: Generate text/code
//! - envision: Vision/multimodal tasks

use clap::{Parser, Subcommand};
use colored::Colorize;
use pronax::cli::{ForgeCommand, IgniteCommand, EnvisionCommand, SynthesizeCommand};

#[derive(Parser)]
#[command(name = "pronax")]
#[command(about = "ProNax AI - 3D Spatial AI Engine", long_about = "
ProNax AI: Next-generation neural inference framework with 3D spatial intelligence.
Built for sub-millisecond latency and production-grade reliability.

Unique Commands:
  forge    - Download and prepare neural models
  ignite   - Launch inference server with spatial awareness
  synthesize - Generate text, code, and embeddings
  envision - Vision and multimodal AI tasks

Get started: pronax forge gemma-4-9b-it
")]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// Download and prepare neural models with 3D spatial optimization
    Forge(ForgeCommand),
    
    /// Launch inference server with spatial awareness
    Ignite(IgniteCommand),
    
    /// Generate text, code, and embeddings
    Synthesize(SynthesizeCommand),
    
    /// Vision and multimodal AI tasks
    Envision(EnvisionCommand),
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let cli = Cli::parse();
    
    println!("{}", "
╔═══════════════════════════════════════════════════════════════════════════════╗
║                           🧠  PRONAX AI                                        ║
║                      3D SPATIAL AI ENGINE                                       ║
╚═══════════════════════════════════════════════════════════════════════════════╝
".bold().cyan());
    
    match cli.command {
        Commands::Forge(cmd) => cmd.execute().await?,
        Commands::Ignite(cmd) => cmd.execute().await?,
        Commands::Synthesize(cmd) => cmd.execute().await?,
        Commands::Envision(cmd) => cmd.execute().await?,
    }
    
    Ok(())
}
