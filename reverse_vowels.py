def reverse_vowels(s):
    # Create a list of vowels from the input string
    vowels = [char for char in s if char in "aeiouAEIOU"]

    # Reverse the list of vowels
    vowels.reverse()

    # Replace vowels in the string with the reversed vowels
    result = []
    vowel_idx = 0
    for char in s:
        if char in "aeiouAEIOU":
            result.append(vowels[vowel_idx])
            vowel_idx += 1
        else:
            result.append(char)

    # Convert the result list back to a string
    return ''.join(result)

# Test cases
print(reverse_vowels("Hello!"))                        # 'Holle!'
print(reverse_vowels("Tomatoes"))                      # 'Temotaos'
print(reverse_vowels("Reverse Vowels In A String"))    # 'RivArsI Vewols en e Streng'
print(reverse_vowels("aeiou"))                         # 'uoiea'
print(reverse_vowels("why try, shy fly?"))             # 'why try, shy fly?'
