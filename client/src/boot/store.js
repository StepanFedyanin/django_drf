import { boot } from 'quasar/wrappers'

// "async" is optional;
// more info on params: https://v2.quasar.dev/quasar-cli/boot-files
export default boot(async ({ store }) => {
    // For Vuex
    if (window.__INITIAL_STATE__) store.replaceState(Object.assign(store.state, window.__INITIAL_STATE__.data));
})
