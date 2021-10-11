import os
import logging
import azure.functions as func
import ocrmypdf
def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')

    # test code for OCR
    try:
        file = req.files.get('file')
        file.save('/tmp/1.pdf')
    except ValueError:
        pass

    text_output = ''
    if file:
        # if __name__ == '__main__':  # To ensure correct behavior on Windows and macOS
        logging.info('Attempting OCR')
        ocrmypdf.ocr('/tmp/1.pdf', '/tmp/1-ocr.pdf', deskew=True, sidecar="/tmp/ocr.txt")

        with open('/tmp/ocr.txt') as f:
            text_output = f.read()

    return func.HttpResponse(text_output)
