def process_sequence(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        
        numbers = list(map(float, content.split()))
        
        in_range_count = sum(-3 <= num <= 3 for num in numbers)
        
        out_of_range_count = len(numbers) - in_range_count
        
        total_count = len(numbers)
        in_range_percentage = (in_range_count / total_count) * 100
        out_of_range_percentage = (out_of_range_count / total_count) * 100
        
        print(f"Values between -3 and 3: {'|' * int(in_range_percentage // 2)} {in_range_percentage:.2f}%")
        print(f"Values outside -3 and 3: {'|' * int(out_of_range_percentage // 2)} {out_of_range_percentage:.2f}%")

process_sequence("sequence.txt")
