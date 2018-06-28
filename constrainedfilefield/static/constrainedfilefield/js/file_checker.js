function humanReadableSize(bytes) {
    units = ['Bytes', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']

    var i = 0
    while (bytes >= 1024) {
        bytes /= 1024
        i++
    }

    return bytes.toFixed(2) + ' ' + units[i]
}

function validateFileSize(input, min, max, message) {
    var size = input.files[0].size;
    var small = (min > 0) && (size < min);
    var large = (max > 0) && (size > max);
    if (small || large) {
        message = message || "File size ({size}) is too "
        message += small ? "low" : "large";
        message += ". Please upload a file of at "
        message += small ? "least" : "most";
        message += " {limit}."
        alert(message.replace('{size}', humanReadableSize(input.files[0].size)).replace('{limit}', humanReadableSize(small ? min : max)));
        input.value = '';
    }
}
