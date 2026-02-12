# HAZEL - High-Assurance Zone-Evaluation Logic
## Trading Signal Advisor Bot

A modular, expandable trading advisor bot designed for Expert Option and other platforms. HAZEL generates intelligent trading signals (BUY, SELL, HOLD) using advanced technical analysis across multiple timeframes (5 seconds to 1 minute).

### Features

- **Multi-Timeframe Analysis**: Supports 5-second to 1-minute intervals
- **Technical Indicators**: RSI, MACD, Bollinger Bands, Stochastic, Moving Averages
- **Signal Generation**: BUY, SELL, HOLD recommendations
- **Modular Architecture**: Easy to expand with new strategies and assets
- **Termux Optimized**: Lightweight, runs efficiently on mobile Linux environments
- **Real-time Monitoring**: Async data handling for multiple assets
- **Configurable**: Easy asset and strategy configuration

### Installation

```bash
pip install -r requirements.txt
```

### Project Structure

hazel/
├── src/
│   ├── __init__.py
│   ├── main.py                 # Main bot runner
│   ├── config.py               # Configuration management
│   ├── data_handler.py         # Market data fetching
│   ├── indicators/
│   │   ├── __init__.py
│   │   ├── rsi.py              # RSI indicator
│   │   ├── macd.py             # MACD indicator
│   │   ├── bollinger_bands.py  # Bollinger Bands
│   │   ├── stochastic.py       # Stochastic indicator
│   │   └── moving_average.py   # Moving averages
│   ├── strategies/
│   │   ├── __init__.py
│   │   ├── base_strategy.py    # Base strategy class
│   │   ├── momentum_strategy.py # Momentum-based strategy
│   │   ├── mean_reversion.py   # Mean reversion strategy
│   │   └── hybrid_strategy.py  # Combined indicators
│   ├── signals/
│   │   ├── __init__.py
│   │   └── signal_generator.py # Signal generation engine
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py           # Logging utilities
│   │   └── validators.py       # Data validation
│   └── alerts/
│       ├── __init__.py
│       └── notifier.py         # Alert notifications
├── tests/
│   ├── __init__.py
│   ├── test_indicators.py
│   ├── test_strategies.py
│   └── test_signals.py
├── requirements.txt
├── README.md
├── .gitignore
└── config.json                 # Configuration file

### Quick Start

1. Configure your assets and indicators in config.json
2. Run the main bot: python src/main.py

### Signal Types

- **BUY**: Strong bullish signal, entry opportunity
- **SELL**: Strong bearish signal, exit/short opportunity
- **HOLD**: Neutral or uncertain signal, wait for clarity

### Roadmap

- [ ] Real-time data integration
- [ ] Multiple asset support
- [ ] Strategy backtesting
- [ ] Performance analytics
- [ ] Machine learning enhancements
- [ ] Mobile notifications

### License

MIT License

### Author

TOXICCANDYme
