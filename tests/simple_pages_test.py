# """This test the homepage"""
#
#
# def test_request_main_menu_links(client):
#     """This makes the index page"""
#     response = client.get("/")
#     assert response.status_code == 200
#     assert b'href="/about"' in response.data
#     assert b'href="/welcome"' in response.data
#     assert b'href="/login"' in response.data
#     assert b'href="/register"' in response.data
#
#
# def test_request_index(client):
#     """This makes the index page"""
#     response = client.get("/")
#     assert response.status_code == 200
#     assert b"Index" in response.data
#
#
# def test_request_about(client):
#     """This makes the index page"""
#     response = client.get("/about")
#     assert response.status_code == 200
#     assert b"About" in response.data
#
#
# def test_request_page1(client):
#     """This makes the index page"""
#     response = client.get("/welcome")
#     assert response.status_code == 200
#     assert b"Welcome" in response.data
#
#
# def test_request_page_not_found(client):
#     """This makes the index page"""
#     response = client.get("/page5")
#     assert response.status_code == 404
#
#
# def test_request_register(client):
#     """This makes the register page"""
#     response = client.get("/register")
#     assert response.status_code == 200
#     assert b"Register" in response.data
#
#
# def user_dashboard_access_approved(client):
#     response = client.get("/dashboard")
#     assert response.status_code == 200
#     return client.get('/dashboard', follow_redirects=True)
#
#
# def user_dashboard_access_deny(client):
#     response = client.get("/dashboard")
#     assert response.status_code == 403
#     return client.get('/dashboard', follow_redirects=False)
#
#
# def test_upload_csvfile_access_denied(client):
#     response = client.get("/upload", follow_redirects=False)
#     assert response.status_code == 404
