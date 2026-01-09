def bubble_sort_visual(numbers):
    print("Starting Bubble Sort Animation:\n")

    n = len(numbers)
    pass_num = 1

    for i in range(n - 1):
        print(f"Pass {pass_num}:")
        pass_num += 1

        for j in range(n - i - 1):
            # Print comparison
            print("Comparing:", numbers[j], "and", numbers[j+1])
            print(" ".join(f"{x:2}" for x in numbers))

            # Swap if needed
            if numbers[j] > numbers[j+1]:
                print(" --> Swap!")
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            else:
                print(" --> No swap")

            # Show list after each step
            print(" ".join(f"{x:2}" for x in numbers))
            print()

        print("-" * 40)

    print("Final sorted list:")
    print(numbers)
grid=[45, 3, 58, 14, 37, 8, 40]
bubble_sort_visual(grid)