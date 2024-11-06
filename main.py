from services.example_factory import ExampleFactory
if __name__ == '__main__':
        example_type = ""
        while example_type != "q":
            print("1.Test example\n2.Singleton example\n")

            example_type = input("Please choose an example(enter the associated number, enter 'q' to quit): ):")
            example = ExampleFactory.get_example(example_type)
            if example is not None:
                example.run()


