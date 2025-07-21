def sort_dicts_by_key_manual(data, key):
    sorted_list = []
    for item in data:
        inserted = False
        for i in range(len(sorted_list)):
            if item[key] < sorted_list[i][key]:
                sorted_list.insert(i, item)
                inserted = True
                break
        if not inserted:
            sorted_list.append(item)
    return sorted_list



'''Using GitHub Copilot, the AI-suggested function to sort a list of dictionaries is highly concise and leverages Python's built-in sorted() function with a lambda expression.
This approach is both readable and efficient, operating with an average time complexity of O(n log n).

In contrast, the manually written implementation uses a custom insertion-based sorting algorithm.
While educational, this method is significantly less efficient, with a time complexity of approximately O(n²) in the worst case.
Additionally, the manual code is more verbose, harder to maintain, and prone to bugs if the logic is not carefully implemented.

Overall, the AI-generated code is more efficient and adheres to Pythonic best practices.
It demonstrates how tools like Copilot can quickly produce clean and optimized solutions by recognizing common patterns.
However, understanding the underlying logic—as shown in the manual version—is still important for learning and debugging complex edge cases that AI might not handle gracefully.'''
