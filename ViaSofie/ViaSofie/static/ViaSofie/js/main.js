/**
 * Created by Tim on 17/05/2016.
 */
function makeSlider(elementId, lowerId, upperId, min, max, start, stop) {
        var nonLinearSlider = document.getElementById(elementId);

        var lowerValue = document.getElementById(lowerId),
                upperValue = document.getElementById(upperId),
                handles = nonLinearSlider.getElementsByClassName('noUi-handle');

        noUiSlider.create(nonLinearSlider, {
            connect: true,
            behaviour: 'tap',
            start: [start, stop],
            step: 1,
            range: {
                'min': [min],
                'max': [max]
            }
        });


        // Display the slider value and how far the handle moved
        // from the left edge of the slider.
        nonLinearSlider.noUiSlider.on('update', function (values, handle) {
            if (!handle) {
                lowerValue.value = parseInt(values[handle]);
            } else {
                upperValue.value = parseInt(values[handle]);
            }
        });

        function changeValue() {
            nonLinearSlider.noUiSlider.set([parseFloat(lowerValue.value), parseFloat(upperValue.value)]);
        }

        lowerValue.oninput = changeValue;
        lowerValue.onpropertychange = changeValue; // for IE8

        upperValue.oninput = changeValue;
        upperValue.onpropertychange = changeValue; // for IE8
    }