const ajax = {
    timeout: process.env.AJAX_TIMEOUT,
    responseType: process.env.AJAX_RESPONSE_TYPE,
    responseEncoding: process.env.AJAX_ENCODING
};

const cache = {
    storage: process.env.CACHE_STORAGE
};

const serviceUrl = {
    selfUrl: process.env.SERVICE_SELF_URL,
    url: process.env.SERVICE_URL,
    protocol: process.env.SERVICE_PROTOCOL,
    port: process.env.SERVICE_PORT,
    api: process.env.SERVICE_API,
    localPath: '//localhost',
    onLocal: (process.env.SERVICE_ON_LOCAL === 'true')
}

let urlPath = `${serviceUrl.url}${serviceUrl.api}`;
if (process.env.CLIENT) {
    if (serviceUrl.onLocal || window.location.hostname === 'localhost') {
        urlPath = `${serviceUrl.localPath}:${serviceUrl.port}${serviceUrl.api}`;
    }
}

const app = {
    url: `${serviceUrl.protocol}://${serviceUrl.url}${serviceUrl.api}`,
}
let selfPath = `https:${serviceUrl.selfUrl}`;

export {
    ajax,
    app,
    cache,
    urlPath,
    selfPath,
};