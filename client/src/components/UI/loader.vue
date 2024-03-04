<template>
	<div>
		<div :class="['loader', show?'active':null]">
			<slot></slot>
		</div>
	</div>
</template>

<script>
export default {
	name: 'loader',
	props: {
		show: {
			type: Boolean,
			default() {
				return false
			}
		}
	}
}
</script>
