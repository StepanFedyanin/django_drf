/* eslint-disable */
// https://github.com/michael-ciniawsky/postcss-load-config

module.exports = {
    plugins: {
        'postcss-mixins': {},
        'postcss-nested': {},
        'postcss-simple-vars': {},
        'postcss-hexrgba': {},
        'postcss-color-function': {},
        'postcss-font-weights': {},
        'postcss-inline-svg': {
            paths: ['./src']
        },
        'postcss-math': {
            functionName: 'calculate'
        },
        'postcss-conditionals': {},
        'postcss-preset-env': {}
    }
}
