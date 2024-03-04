<template>
  <div :class="['dish', showDish?'active':null]" @click="hiddenDish">
    <div class="dish__wrapper" ref="dishWrapper" @click.stop>
      <div class="dish__drop" v-touch-pan.prevent.mouse="scrollListener"></div>
      <div class="dish__content">
        <div class="dish__cover">
          <img
            :src="dish?.image"
            alt=""/>
        </div>
        <div class="dish__info">
          <span>{{dish?.name}}</span>
          {{250}} г
        </div>
        <div class="dish__description p">
          {{dish?.description}}
        </div>
      </div>
      <button class="dish__btn btn">Добавить <span>{{dish?.price}} р</span></button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'dish',
  props:{
    showDish:{
      type: Boolean,
      default() {
        return false
      }
    },
    dish: {
      type: Object,
      default () {
        return null
      }
    },

  },
	data() {
		return{
			scrollMixing: 15
		}
	},
	watch: {
		showDish: {
			immediate: true,
			handler(to) {
				const body = document.getElementsByTagName('body')[0]
				this.scrollMixing = 0;
				if (to){
					body.classList.add('body-freeze')
				}else {
					body.classList.remove('body-freeze')
				}
			}
		},
	},
  methods: {
		scrollListener(value){
			this.scrollMixing = value.offset.y
			if (value.offset.y > 200){
				this.hiddenDish();
				this.scrollMixing = 0
			}else if (value.isFinal) {
				this.scrollMixing = 0
			}
			this.$refs.dishWrapper.style.transform  =  `translateY(${this.scrollMixing}px)`;
		},
    hiddenDish () {
      this.$emit('hiddenDish', false)
    }
  }
}
</script>
