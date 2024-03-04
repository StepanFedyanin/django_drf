<template>
	<div class="catalog__dish">
		<div class="catalog__dish--info">
			{{ dish.name }}
			<span>{{ dish.price }} ₽</span>
		</div>
		<div class="catalog__dish--image">
			<img :src="dish.image">
		</div>
		<div class="catalog__dish--btn">
			<button class="btn h4" v-if="dish.quantity===0" @click.stop="postAddOrder(dish.id)">Добавить</button>
			<div v-else class="catalog__dish--quantity">
				<button class="catalog__dish--minus" @click.stop="changeQuantity(dish.quantity - 1, dish.order_item)"></button>
				{{dish.quantity}}
				<button class="catalog__dish--plus" @click.stop="changeQuantity(dish.quantity + 1, dish.order_item)"></button>
			</div>
		</div>
	</div>
</template>

<script>
import {app} from '@/services'

export default {
	name: 'dish-card-catalog',
	props:{
		paramsDish:{
			type: Object,
			default(){
				return {}
			}
		}
	},
	data(){
		return {
			dish: this.paramsDish
		}
	},
	methods:{
		changeQuantity(quantity, order_item){
			if (quantity < 1){
				const params = {id: order_item}
				this.postRemoveOrder(params)
			}else {
				const params = {order_item: order_item,quantity: quantity }
				this.postUpdateOrder(params)
			}
		},
		postAddOrder(dish_id){
			const params = {
				restaurant:this.$route.params.id,
				dish:dish_id
			}
			app.sendOrderItem(params).then(data=>{
				this.dish = data;
			}).catch((err)=>{
				console.log(err)
			})
		},
		postUpdateOrder(params){
			app.sendUpdateOrderItem(params).then(data=>{
				this.dish = data
			}).catch(err=>{
				console.log(err)
			})
		},
		postRemoveOrder(params){
			app.sendRemoveOrderItem(params).then(data=>{
				this.dish = data
			}).catch(err=>{
				console.log(err)
			})
		},
	}
}
</script>
