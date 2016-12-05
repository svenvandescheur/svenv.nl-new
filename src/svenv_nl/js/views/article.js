/**
 * Module containing classes for article views.
 * @module
 */
import BEM from 'bem.js';
import { AbstractDetailView } from './abstractdetail';
import { Parallax } from '../lib/parallax';


/**
 * Class containing logic for article views.
 * @class
 */
class ArticleView extends AbstractDetailView {
    /**
     * Constructor
     * Add Article to the page if required.
     */
    constructor() {
        super('view-article');
    }
}


// Initiate
new ArticleView();
