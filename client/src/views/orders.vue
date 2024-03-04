<template>
	<div class="wrapper">
		<TopBar class="q-mb-lg"/>
		<div class="order wrapper__content">
			<div
				v-if="orders?.order_dish?.length > 0"
				class="order__content"
			>
				<DishCardOrder
					v-for="dish in orders.order_dish"
					:key="`order-${dish.id}`"
					:paramsDish="dish"
				/>
			</div>
			<div v-else class="order__empty h2">
				Корзина пуста!
				<q-btn color="primary" @click="next()">
					Вернуться в каталог
				</q-btn>
			</div>
		</div>
	</div>
</template>

<script>
import {app} from '@/services'
import TopBar from "@/components/topBar.vue";
import DishCardOrder from "@/components/dish-card-order.vue";

export default {
	name: 'orders',
	components: {DishCardOrder, TopBar},
	data(){
		return{
			orders: {}
		}
	},
	created() {
		this.getOrders();
	},
	methods:{
		getOrders(){
			app.getOrders().then(res=>{
				this.orders = res;
			}).catch(error=>{
				console.log(error)
			})
		},
		next (name='restaurant', params = {id:1}) {
			this.$router.push({name,params })
		}
	}
}
</script>
