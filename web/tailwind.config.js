/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,js}",
    "./*.html",
    "./*.js"
  ],
  theme: {
    extend: {
      colors: {
        'pronax-cyan': '#00d4ff',
        'pronax-green': '#00ff88',
        'pronax-dark': '#0f0f23',
        'pronax-darker': '#1a1a2e'
      },
      animation: {
        'typing': 'typing 1.4s infinite ease-in-out',
        'slide-in': 'slideIn 0.3s ease-out',
        'rotate-3d': 'rotate3d 10s infinite linear',
        'pulse-cyan': 'pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'pulse-green': 'pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite'
      },
      keyframes: {
        typing: {
          '0%, 80%, 100%': {
            transform: 'scale(0.8)',
            opacity: '0.5'
          },
          '40%': {
            transform: 'scale(1)',
            opacity: '1'
          }
        },
        slideIn: {
          'from': {
            opacity: '0',
            transform: 'translateY(10px)'
          },
          'to': {
            opacity: '1',
            transform: 'translateY(0)'
          }
        },
        rotate3d: {
          'from': {
            transform: 'rotateX(0deg) rotateY(0deg)'
          },
          'to': {
            transform: 'rotateX(360deg) rotateY(360deg)'
          }
        }
      },
      backgroundImage: {
        'gradient-3d': 'linear-gradient(135deg, #0f0f23 0%, #1a1a2e 100%)',
        'gradient-cyan': 'linear-gradient(45deg, #00d4ff, #00ff88)',
        'gradient-blue': 'linear-gradient(45deg, #00d4ff, #3b82f6)',
        'gradient-chat': 'linear-gradient(45deg, #00d4ff, #3b82f6)',
        'gradient-user': 'linear-gradient(45deg, #00d4ff, #06b6d4)'
      },
      boxShadow: {
        'neon-cyan': '0 0 20px rgba(0, 212, 255, 0.5)',
        'neon-green': '0 0 20px rgba(0, 255, 136, 0.5)',
        'glass': '0 4px 30px rgba(0, 0, 0, 0.1)',
        'glass-border': 'inset 0 0 0 1px rgba(255, 255, 255, 0.1)'
      },
      backdropBlur: {
        'glass': '10px'
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}
