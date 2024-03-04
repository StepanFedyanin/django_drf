<template>
	<div class="order__dish">
		<div class="order__dish--cell m--image">
			<img :src="dish.image" alt=""/>
		</div>
		<div class="order__dish--cell">
			{{dish.name}}
		</div>
		<div class="order__dish--cell">
			{{dish.price}} ₽
		</div>
		<div class="order__dish--cell m--quantity">
			{{dish.quantity}}
		</div>
		<div class="order__dish--cell">
			<q-btn class="order__dish--btn m--plus" color="primary"></q-btn>
			<q-btn class="order__dish--btn m--minus" color="primary"></q-btn>
		</div>
	</div>
</template>

<script>
import {app} from '@/services'
export default {
	name: 'dish-card-order',
	props:{
		paramsDish:{
			type: Object,
			default(){
				return {}
			}
		},
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
