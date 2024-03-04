import { vMaska } from 'maska'
import {boot} from "quasar/wrappers";
export default boot(async ({ app, router }) => {
    if (process.env.CLIENT) {
        app.directive('Maska', vMaska);
    }
})