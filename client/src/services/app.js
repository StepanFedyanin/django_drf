import {app as settings} from '../settings/index';
import { REST, RESTError } from './rest'

export default class extends REST {
    static get settings () {
        return settings
    }

    static getRestaurant (id) {
        return this._get(`restaurants/${id}`, {}, {}).then(data=>{
            return data
        }).catch((error)=>{
            throw new RESTError(error, 'не удалось получить ресторан')
        })
    }
    static getRestaurantCategory (id) {
        return this._get(`restaurants/${id}/category`, {}, {}).then(data=>{
            return data
        }).catch((error)=>{
            throw new RESTError(error, 'не удалось получить категории блюд')
        })
    }
    static getDish (id) {
        return this._get(`restaurants/dish/${id}`, {}, {}).then(data=>{
            return data
        }).catch((error)=>{
            throw new RESTError(error, 'не удалось получить блюдо')
        })
    }
    
    static sendPhoneLogin (params) {
        return this._post(`user/login/create_code`, {}, params).then(data=>{
            return data
        }).catch((error)=>{
            throw new RESTError(error, 'не удалось отправить запрос на получение кода')
        })
    }
    
    static sendCodeLogin (params) {
        return this._post(`user/login/post_code`, {}, params).then(data=>{
            return data
        }).catch((error)=>{
            throw new RESTError(error, 'не удалось отправить код')
        })
    }
    
    static sendOrderItem (params){
        return this._post(`restaurants/order/add_dish`, {}, params).then(data=>{
            return data
        }).catch((error)=>{
            throw new RESTError(error, 'не удалось добавить в заказ')
        })
    }
    
    static sendUpdateOrderItem(params){
        return this._post(`restaurants/order/change_quantity_dish`, {}, params).then(data=>{
            return data
        }).catch((error)=>{
            throw new RESTError(error, 'не удалось добавить в заказ')
        })
    }
    
    static sendRemoveOrderItem(params){
        return this._post(`restaurants/order/remove_dish`, {}, params).then(data=>{
            return data
        }).catch((error)=>{
            throw new RESTError(error, 'не удалось добавить в заказ')
        })
    }
    
    
    static getOrders(){
        return this._get(`restaurants/order/1`, {}, {}).then(data=>{
            return data
        }).catch((error)=>{
            throw new RESTError(error, 'не удалось получить заказ')
        })
    }
}
