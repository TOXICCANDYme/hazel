# Configuration Management

class Config:
    """
    Configuration management for assets, timeframes, indicators, and data sources
    """

    def __init__(self):
        self.assets = []  # List of assets to monitor
        self.timeframes = []  # List of timeframes for analysis
        self.indicators = []  # List of indicators to use
        self.data_sources = {}  # Dictionary for data sources

    def add_asset(self, asset):
        self.assets.append(asset)

    def set_timeframes(self, timeframes):
        self.timeframes = timeframes

    def add_indicator(self, indicator):
        self.indicators.append(indicator)

    def add_data_source(self, name, source):
        self.data_sources[name] = source

# Example usage:
# config = Config()
# config.add_asset('AAPL')
# config.set_timeframes(['1m', '5m', '1h'])
# config.add_indicator('RSI')
# config.add_data_source('Yahoo Finance', 'https://finance.yahoo.com')