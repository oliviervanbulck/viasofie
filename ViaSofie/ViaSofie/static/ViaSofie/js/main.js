/**
 * Created by Tim on 17/05/2016.
 */

/**
 * Function to make a slider in forms
 */
function makeSlider(elementId, lowerId, upperId, min, max, step, lowerFormattedId, upperFormattedId) {
    // Optionele parameters!
    lowerFormattedId = lowerFormattedId || null;
    upperFormattedId = upperFormattedId || null;

    var nonLinearSlider = document.getElementById(elementId);

    var lowerValue = document.getElementById(lowerId),
        upperValue = document.getElementById(upperId),
        lowerFormatted = (lowerFormattedId ? document.getElementById(lowerFormattedId) : null),
        upperFormatted = (upperFormattedId ? document.getElementById(upperFormattedId) : null);

    noUiSlider.create(nonLinearSlider, {
        connect: true,
        behaviour: 'tap',
        //start: [start, stop],
        start: [parseInt(lowerValue.value), parseInt(upperValue.value)],
        step: step,
        range: {
            'min': [min],
            'max': [max]
        }
    });

    // Display the slider value and how far the handle moved
    // from the left edge of the slider.
    nonLinearSlider.noUiSlider.on('update', function (values, handle) {
        var tmp = parseInt(values[handle]);
        if (!handle) {
            lowerValue.value = tmp;
            if (lowerFormatted != null) {
                lowerFormatted.innerHTML = tmp.toLocaleString();
            }
        } else {
            upperValue.value = tmp;
            if (upperFormatted != null) {
                upperFormatted.innerHTML = tmp.toLocaleString();
            }
        }
    });
}
