const webpack = require('webpack');
const path = require('path');
const ManifestPlugin = require('webpack-manifest-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
// import 'normalize.css'
// import 'react-notifications/lib/notifications.css';

// input dir
const APP_DIR = path.resolve(__dirname, './MoneyTime');

// output dir
const BUILD_DIR = path.resolve(__dirname, '../MoneyTime/staticfiles/media');


const config = {
  node: {
    fs: 'empty',
  },
  entry: {
    // theme: APP_DIR + '/javascripts/theme.js',
    common: APP_DIR + '/app.js',
  },
  output:  {
    path: BUILD_DIR,
    filename: '[name].js'
  },
  resolve: {
    extensions: [
      '.js',
      '.jsx',
    ],
    alias: {
      webworkify: 'webworkify-webpack',
    },
  },
  module: {
    loaders: [
      {
        test: /\.jsx?$/,
        loader: 'babel-loader',
        exclude: /node_modules/,
        include: APP_DIR,
        query: {
          plugins: ['transform-runtime'],
          presets: ['es2015', 'stage-0', 'react']
        }
      },
      // Extract css files
      {
        test: /\.css$/,
        include: APP_DIR,
        loader: ExtractTextPlugin.extract({
          use: ['css-loader'],
          fallback: 'style-loader',
        }),
      },
      // Optionally extract less files
      // or any other compile-to-css language
      {
        test: /\.less$/,
        include: APP_DIR,
        loader: ExtractTextPlugin.extract({
          use: ['css-loader', 'less-loader'],
          fallback: 'style-loader',
        }),
      },
      /* for css linking images */
      {
        test: /\.png$/,
        loader: 'url-loader?limit=100000',
      },
      {
        test: /\.jpg$/,
        loader: 'file-loader',
      },
      {
        test: /\.gif$/,
        loader: 'file-loader',
      },
      /* for font-awesome */
      {
        test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/,
        loader: 'url-loader?limit=10000&mimetype=application/font-woff',
      },
      {
        test: /\.(ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
        loader: 'file-loader',
      },
    ]
  },
  externals: {
    cheerio: 'window',
    'react/lib/ExecutionEnvironment': true,
    'react/lib/ReactContext': true,
  },
  plugins: [
    // new ManifestPlugin(),
    new CleanWebpackPlugin(['dist']),
    new ExtractTextPlugin('[name].css'),
  ],
}

module.exports = config;
