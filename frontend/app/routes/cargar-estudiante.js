import Ember from "ember";

export default Ember.Route.extend({



    model() {


        return this.store.createRecord("estudiante");
    },

    actions: {
        regresar() {
            this.transitionTo("cargarRepresentante");
        },
        willTransition: function() {
            if (this.currentModel.get("isNew")) {
                this.get("currentModel").deleteRecord();
            }
        }
    }
});