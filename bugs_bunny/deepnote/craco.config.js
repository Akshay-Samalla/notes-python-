const NodePolyfillPlugin = require('node-polyfill-webpack-plugin');

module.exports = {
  webpack: {
    configure: (webpackConfig, { env, paths }) => {
      // Resolve fallbacks for Node.js built-in modules
      webpackConfig.resolve.fallback = {
        path: require.resolve('path-browserify'),
        fs: false,
        crypto: require.resolve('crypto-browserify'),
        stream: require.resolve('stream-browserify'),
        buffer: require.resolve('buffer/'),
        process: require.resolve('process/browser'),
        vm: require.resolve('vm-browserify'), // Polyfill vm instead of stubbing
        url: require.resolve('url/'),
        child_process: false,
        zlib: require.resolve('browserify-zlib'),
      };

      // Add NodePolyfillPlugin
      webpackConfig.plugins.push(new NodePolyfillPlugin());

      // Ensure buffer alias overrides conflicting resolutions
      webpackConfig.resolve.alias = {
        ...webpackConfig.resolve.alias,
        buffer: require.resolve('buffer/'),
      };

      // Add extensions for ESM strictness
      webpackConfig.resolve.extensions = [
        ...webpackConfig.resolve.extensions,
        '.js',
        '.mjs',
      ];

      // Target browser environment
      webpackConfig.target = 'web';

      return webpackConfig;
    },
  },
};  