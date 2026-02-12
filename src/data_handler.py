import requests
import websocket
import json
import threading

class DataHandler:
    def __init__(self, binance_base_url="https://api.binance.com/api/v3/", ws_url="wss://stream.binance.com:9443/ws"):
        self.binance_base_url = binance_base_url
        self.ws_url = ws_url

    def fetch_data(self, endpoint, params=None):
        url = f"{self.binance_base_url}{endpoint}"
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching data: {response.status_code} {response.text}")

    def on_message(self, ws, message):
        print(f"Received message: {message}")
        # Handle incoming WebSocket message here

    def on_error(self, ws, error):
        print(f"WebSocket error: {error}")

    def on_close(self, ws):
        print("WebSocket connection closed")

    def on_open(self, ws):
        print("WebSocket connection opened")
        # You can send a message to the server here if needed

    def start_websocket(self):
        ws = websocket.WebSocketApp(
            self.ws_url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        ws.on_open = self.on_open
        ws.run_forever()

    def run(self):
        # Example to fetch market data
        try:
            market_data = self.fetch_data("ticker/price", {"symbol": "BTCUSDT"})
            print(market_data)
        except Exception as e:
            print(e)

        # Start WebSocket in a separate thread
        ws_thread = threading.Thread(target=self.start_websocket)
        ws_thread.start()


if __name__ == "__main__":
    data_handler = DataHandler()
    data_handler.run()