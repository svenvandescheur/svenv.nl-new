/**
 * Module containing classes for simplepage views.
 * @module
 */
import BEM from 'bem.js';
import { AbstractDetailView } from './abstractdetail';
import { Parallax } from '../lib/parallax';


/**
 * Class containing logic for simplePage views.
 * @class
 */
class SimplePageView extends AbstractDetailView {
    /**
     * Constructor
     * Add SimplePage to the page if required.
     */
    constructor() {
        super('view-simplepage');
    }
}


// Initiate
new SimplePageView();
