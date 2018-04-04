function validateFileSize(input, min, max, message) {
    var size = input.files[0].size;
    var small = size < min;
    var large = size > max;
    if (small || large) {
        message = message || "File size ({size}) is too "
        message += small ? "low" : "large";
        message += ". Please upload a file of at "
        message += small ? "least" : "most";
        message += " {limit}."
        alert(message.replace('{size}', input.files[0].size).replace('{limit}', small ? min : max));
        input.value = '';
    }
}