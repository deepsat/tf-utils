from tensorflow.keras.models import Model, load_model
import os
import argparse
from pathlib import Path


def keras_to_tf(input_path: Path, output_path: Path):
    model = load_model(input_path)
    model.save(output_path)


def create_arg_parser():
    # Creates and returns the ArgumentParser object

    parser = argparse.ArgumentParser(
        description="Converts keras .h5 model file to tf saved model."
    )
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input", type=Path, help="Path to Keras h5 model."
    )
    parser.add_argument(
        "--output",
        "-o",
        required=False,
        type=Path,
        help="Output folder path.",
        default=Path("tf"),
    )

    return parser


if __name__ == "__main__":
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args()
    input_path, output_path = parsed_args.input, parsed_args.output

    keras_to_tf(input_path, output_path)