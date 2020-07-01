import Ember from "ember";

export default Ember.Route.extend({

    model() {

        let estudiante = this.store.find('estudiante', "1");
        console.log(estudiante)

        let representante = this.store.createRecord('representante', {
            estudiante: estudiante
        });

        representante.save();
        return this.store.createRecord("representante");
    },

    actions: {
        regresar() {
            this.transitionTo("index");
        },
        willTransition: function() {
            if (this.currentModel.get("isNew")) {
                this.get("currentModel").deleteRecord();
            }
        }
    }
});