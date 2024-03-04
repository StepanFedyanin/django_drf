<template>
	<div class="wrapper">
		<TopBar class="q-mb-lg"/>
		<div class="catalog__restaurant p q-mb-lg">{{ restaurant.name }} - {{ restaurant.address }}</div>
		<categoryDish class="q-mb-lg" :select="selectCategory" :categories="category" @changeSelect="changeCategory"/>
		<div v-for="restaurant in restaurant.categorys" :key="`category-${restaurant.id}`" class="catalog__categorys q-mb-md">
			<h2 class="h2 q-my-md" :id="restaurant.category" v-scroll-fire="log">{{ restaurant.category }}</h2>
			<div class="catalog__category">
				<DishCardCatalog
					v-for="dish in restaurant.dish"
					:key="`dish-${dish.id}`"
					@click="getDish(dish.id)"
					:paramsDish="dish"
				/>
			</div>
		</div>
		<dish :dish="selectedDish" :showDish="showDish" @hiddenDish="changeShowDish"/>
	</div>
</template>

<script>
import {app} from '@/services'
import TopBar from "@/components/topBar.vue";
import CategoryDish from "@/components/categoryDish.vue";
import dish from "@/components/dish.vue";
import DishCardCatalog from "@/components/dish-card-catalog.vue";

export default {
	name: 'catalog',
	components: {DishCardCatalog, CategoryDish, TopBar, dish},
	data() {
		return {
			selectedDish: null,
			showDish: false,
			restaurant: [],
			category: [],
			selectCategory: null,
			token: null
		}
	},
	created() {
		this.token = this.$store.state.token
		this.getRestaurant(this.$route.params.id)
		this.getRestaurantCategory(this.$route.params.id)
	},
	methods: {
		getRestaurant(params) {
			app.getRestaurant(params).then((data) => {
				this.restaurant = data;
			}).catch((err => {
				console.log(err)
			}))
		},
		getRestaurantCategory(params) {
			app.getRestaurantCategory(params).then((data) => {
				this.category = data;
				this.selectCategory = data[0].category
				console.log(data)
			}).catch((err => {
				console.log(err)
			}))
		},
		getDish(id) {
			app.getDish(id).then(data => {
				this.selectedDish = data;
				this.changeShowDish(true);
			}).catch(err => {
				console.log(err)
			})
		},
		changeCategory(value) {
			this.selectCategory = value
		},
		changeShowDish(value) {
			this.showDish = value;
		}
	}
}
</script>
