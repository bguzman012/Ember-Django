import DS from "ember-data";
import { validatePresence } from "ember-changeset-validations/validators";

export default DS.Model.extend({
    cedula: DS.attr("string"),
    nombre: DS.attr("string"),
    apellidos: DS.attr("string"),
    fecha: DS.attr("string"),


    validaciones1: {
        cedula: [validatePresence(true)],
        nombre: [validatePresence(true)],
        apellidos: [validatePresence(true)],
        fecha: [validatePresence(true)]
    }
});