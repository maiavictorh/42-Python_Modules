from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        print("\nInitializing Numeric Processor...\n"
              f"Processing data: {data}")
        try:
            return (f"Processed {len(data)} numeric values,"
                    f" sum={sum(data)}, avg={sum(data) / len(data):.1f}")
        except Exception:
            print("\33[31mUh-oh, Something went wrong!\33[0m")

    def validate(self, data: Any) -> bool:
        if type(data) is not list:
            print("\33[33mValidation: Data must be a list\33[0m")
            return False
        for item in data:
            if type(item) is not int:
                print("\33[33mValidation: Data must be list of integers\33[0m")
                return False
            print("\33[32mValidation: Numeric data verified\33[0m")
            return True

    def format_output(self, result: str) -> str:
        if not result:
            result = "Nothing to declare."
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        print("\nInitializing Text Processor...\n"
              f"Processing data: \"{data}\"")
        try:
            return (f"Processed text: {len(data)} characters,"
                    f" {len(data.split())} words")
        except Exception:
            print("\33[31mUh-oh, Something went wrong!\33[0m")

    def validate(self, data: Any) -> bool:
        if type(data) is not str:
            print("\33[33mValidation: Data must be a string\33[0m")
            return False
        print("\33[32mValidation: text data verified\33[0m")
        return True

    def format_output(self, result: str) -> str:
        if not result:
            result = "Nothing to declare"
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
    # print("\nInitializing Log Processor...")


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    numeric_data = [1, 2, 3, 4, 5]
    numeric_processor = NumericProcessor()
    num_process = numeric_processor.process(numeric_data)
    numeric_processor.validate(numeric_data)
    print(numeric_processor.format_output(num_process))

    text_data = "Hello Nexus World"
    text_processor = TextProcessor()
    text_process = text_processor.process(text_data)
    text_processor.validate(text_data)
    print(text_processor.format_output(text_process))

    # print("\n=== Polymorphic Processing Demo ===")

    # print("\nProcessing multiple data types through same interface...")

    # print("\n Foundation systems online. Nexus ready for advanced streams.")
