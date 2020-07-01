import DS from "ember-data";
import { validatePresence } from "ember-changeset-validations/validators";

export default DS.Model.extend({
    estudiante: DS.belongsTo("estudiante"),
    cedula: DS.attr("string"),
    nombre: DS.attr("string"),
    apellidos: DS.attr("string"),
    correo: DS.attr("string"),

});