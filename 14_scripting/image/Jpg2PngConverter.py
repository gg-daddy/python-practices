import argparse
from pathlib import Path

from PIL import Image
from tqdm import tqdm


class Jpg2PngConverter:
    def __init__(self, source_folder, output_folder):
        self.source_folder = Path(source_folder)
        if not self.source_folder.exists():
            raise FileNotFoundError(f"Source folder '{source_folder}' does not exist")
        if self.source_folder.is_file():
            raise FileNotFoundError(f"Source folder '{source_folder}' is a file")

        self.output_folder = Path(output_folder)
        if not self.output_folder.exists():
            self.output_folder.mkdir(parents=True)

    def convert(self):
        with tqdm(
            list(self.source_folder.iterdir()), desc="Converting jpg images to png"
        ) as pbar:
            processed = 0
            for file in pbar:
                if file.suffix.lower() == ".jpg":
                    pbar.set_description(
                        f"Processing {file.name}, {processed} completed"
                    )
                    output_file = self.output_folder / ("new-" + file.stem + ".png")
                    Jpg2PngConverter._convert_file(file, output_file)
                    processed += 1

    @staticmethod
    def _convert_file(input_file, output_file):
        Image.open(input_file).save(output_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert jpg images to png.")
    parser.add_argument(
        "--source",
        required=True,
        type=str,
        help="The source folder containing jpg images.",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=str,
        help="The output folder to save png images.",
    )
    args = parser.parse_args()

    converter = Jpg2PngConverter(args.source, args.output)
    converter.convert()
