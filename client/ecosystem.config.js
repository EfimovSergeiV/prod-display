module.exports = {
    apps: [
      {
        name: 'ProdDisplay',
        port: '3000',
        exec_mode: 'cluster',
        instances: 'max',
        script: './.output/server/index.mjs'
      }
    ]
  }