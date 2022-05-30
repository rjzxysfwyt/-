const webpack = require('webpack')
module.exports = {
    resolve:{},
    plugins: [    　　
      　　new webpack.ProvidePlugin({
      　　　　$: "jquery",
      　　　　jQuery: "jquery"
      　　})
    ],
    module:{}
}