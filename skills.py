"""Skills Assessment: Lists.

To work on an item, uncomment the entire function (including the docstring)
and then run this script. It should output an error that the newly-uncommented
function is now failing its tests.

Edit the function body until you have a solution and the test passes, and then
move on to the next function.

This assessment is DUE TO YOUR ADVISOR BY SUNDAY EVENING.
"""


def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []
    """
    odd_number = []
    even_number = []
    empty_list = []
    for number in number_list:
        if number % 2 == 1:
            odd_number.append(number)
        if number % 2 == 0:
            even_number.append(number)
        if len(even_number) == len(number_list):
            return empty_list

    return odd_number


def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """
    even_number = []
    odd_number = []
    empty_list = []
    for number in number_list:
        if number % 2 == 0:
            even_number.append(number)
        if number % 2 == 1:
            odd_number.append(number)
        if len(odd_number) == len(number_list):
            return empty_list

    return even_number


def print_indeces(my_list):
    """Print the index of each list item, followed by the item itself.
    Do this without using a counting variable. I.e. don't do something
    like this:

    count = 0
    for item in list:
        print count
        count = count + 1

    Output should look like this:

    >>> print_indeces(["Toyota", "Jeep", "Volvo"])
    0 Toyota
    1 Jeep
    2 Volvo

    """
    for index, element in enumerate(my_list):
        print index, element


def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """
    long_words = []
    short_words = []
    for word in word_list:
        if len(word) > 4:
            long_words.append(word)
        if len(word) < 4:
            short_words.append(word)
        if len(short_words) == len(word_list):
            return []
    return long_words


def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

        >>> smallest_int([-5, 2, -5, 7])
        -5

    If the input list is empty, return None:

        >>> smallest_int([]) is None
        True

    """
    smallest = 100
    if len(number_list) == 0:
        return None
    else:
        for number in number_list:
            if number < smallest:
                smallest = number
        return smallest


def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

        >>> largest_int([-5, 2, -5, 7])
        7

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """
    largest = 0
    if len(number_list) == 0:
        return None
    else:
        for number in number_list:
            if number > largest:
                largest = number
        return largest


def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """
    each_divide_inhalf = []
    for number in number_list:
        divided = float(number/2.0)
        each_divide_inhalf.append(divided)
    return each_divide_inhalf


def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """
    word_lengths = []
    for word in word_list:
        length = len(word)
        word_lengths.append(length)

    return word_lengths


def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """
    add_number = 0
    for number in number_list:
        if len(number_list) > 0:
            add_number = add_number + number
        if len(number_list) == 0:
            return 0
    return add_number


def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """
    mult_numbers = 1
    for number in number_list:
        if 0 in number_list:
            return 0
        elif 0 not in number_list:
            mult_numbers = mult_numbers * number
        else:
            if number_list == []:
                return 1

    return mult_numbers


def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python ha a built-in method on lists, `join` -- but this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """
    concatinate_string = ''
    empty_string = ''
    for string in word_list:
        if len(word_list) > 0:
            concatinate_string = concatinate_string + string
        if len(word_list) == 0:
            return empty_string
    return concatinate_string


def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """
    get_sum = 0
    for number in number_list:
        get_sum = get_sum + number
    ave = float(get_sum)/len(number_list)
    return ave


#############################################################################
# END OF SKILLS TEST: You can stop here, or read on to work on advanced problem.

# Uncomment the function below to work on the advanced problem.
# Tip: To comment or uncomment blocks of code, highlight what you want to
#    comment or uncomment, and then CMD+"/" or CTRL-"/"

# def advanced_join_strings(list_of_words):
#     """Return a single string with each word from the input list
#     separated by a comma.

#         >>> advanced_join_strings(["Labrador", "Poodle", "French Bulldog"])
#         'Labrador, Poodle, French Bulldog'

#     If there's only one thing in the list, it should return just that
#     thing, of course:

#         >>> advanced_join_strings(["Pretzel"])
#         'Pretzel'

#     """

#     return ""

# END OF ASSIGNMENT: You can ignore everything below.
##############################################################################

if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s TESTS PASSED. GOOD WORK!" % result.attempted
    print
