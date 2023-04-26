import argparse

from libs.webserver_helper import WebServerHelper


def main():
    parser = argparse.ArgumentParser(prog="HTTPServer",  description="Start http server")
    parser.add_argument("--host", default="0.0.0.0")  # option that takes a value
    parser.add_argument("-p", "--port", default=80, type=int)
    args = parser.parse_args()
    webserver_helper = WebServerHelper(
        is_http=True,
        host=args.host,
        port=args.port
    )
    webserver_helper.start()


if __name__ == "__main__":
    main()
