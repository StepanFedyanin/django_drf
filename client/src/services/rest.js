import ajax from '@/utils/ajax'
import store from '@/store'
class RESTError extends Error {
    constructor (error, message, params = {}) {
        // eslint-disable-next-line no-mixed-operators
        const detail = error.response && error.response.data && (error.response.data.detail || error.response.data.error && error.response.data.error.detail)
        const header = (message || error.message) + (detail ? ': ' + detail : '')
        super(header)
        
        this.name = this.constructor.name
        this.parent = error
        this.detail = detail
        this.response = error.response
        for (const k in params) {
            this[k] = params[k]
        }
        
        if (typeof Error.captureStackTrace === 'function') {
            Error.captureStackTrace(this, this.constructor)
        } else {
            this.stack = (new Error(header)).stack
        }
    }
}

class REST {
    static get settings() {
        throw new Error('settings must be overridden');
    }
    
    static _get (url, params = {}, use_cache = false) {
        return this._request('get', url, params, {}, use_cache)
    }
    
    static _post (url, params, data) {
        return this._request('post', url, params, data)
    }
    
    static _put (url, params, data) {
        return this._request('put', url, params, data)
    }
    
    static _patch (url, params, data) {
        return this._request('patch', url, params, data)
    }
    
    static _delete (url, params, data) {
        return this._request('delete', url, params, data)
    }
    
    static _request (method, url, params = {}, data = {}) {
        return ajax.request({
            method,
            url: `${this.settings.url}/${url}/`,
            params,
            data,
            headers: this._getAuthHeaders()
        }).then((response) => {
            return response.data
        })
    }
    
    static _getAuthHeaders () {
        if (store.state.token) {
            return { Authorization: `Bearer ${store.state.token}` }
        } else {
            return {}
        }
    }
}

export {
    RESTError,
    REST
}
