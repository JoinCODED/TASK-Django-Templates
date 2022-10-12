## Task

Continue working on the previous task repository, [Views and URLs](https://warehouse.joincoded.com/assignments/views-and-urls).

## Detail Page

1. Go to `products/views.py` and add a `get_product` view function that takes in a request and `product_id`, and renders a template named `product_detail.html` (you might find [this link useful](https://docs.djangoproject.com/en/4.0/intro/tutorial03/#a-shortcut-render)).
2. Fetch the product object based on the ID received in the parameter.
3. Add the following context to be injected into your template:
   - `name`: the product's name as a string.
   - `description`: the product's description as a string.
   - `price`: the product's price as an integer.
4. Add your `get_product` view to your URLs.
5. Name it `product-detail`, and make sure to add `product_id` to the path.
6. Create a `templates` folder inside of `products` and add a `product_detail.html` file.
7. The template should render the entire context passed to it.
8. Run the server and check out your beautiful products.
9. Commit your code and push.

## List Page

1. Go to `products/views.py` and add a `get_products` view function that takes in a request and renders a template named `product-list.html`.
2. Your context should include the details of all products.
3. Add your `get_products` view to your URLs and name it `product-list`.
4. Create a `templates` folder inside of `products` and add an `product-list.html` file.
5. The template should render the entire context passed to it.
6. Use [this link](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#cycle) to see how to loop over objects in DTL.
7. Run the server and check out your beautiful products.
8. Commit your code and push.

## Detail View Bonus

- In the detail view, wrap your fetch in a try-except block and raise an Http404 if the ice cream id does not exist.

## List View Bonus

- Add a button that links each product in the list view that redirects the user to the detail page.
