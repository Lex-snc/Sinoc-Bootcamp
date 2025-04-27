from locust import HttpUser, task, between

class PharmacyUser(HttpUser):
    # Wait time between tasks for each user (1 to 5 seconds)
    wait_time = between(1, 5)

    # Host URL for the Flask application
    host = "http://localhost:5000"

    @task(3)
    def get_medicines_suppliers(self):
        """
        Task to simulate GET request to /medicines/suppliers endpoint.
        This endpoint retrieves medicines with supplier details.
        Given a higher weight (3) as it's likely a frequently accessed endpoint.
        """
        self.client.get("/medicines/suppliers")

    @task(2)
    def get_customers_prescriptions(self):
        """
        Task to simulate GET request to /customers/prescriptions endpoint.
        This endpoint retrieves customers with their prescriptions.
        Given a weight of 2 as it may be accessed moderately.
        """
        self.client.get("/customers/prescriptions")

    @task(1)
    def get_medicines_prescription_counts(self):
        """
        Task to simulate GET request to /medicines/prescription-counts endpoint.
        This endpoint retrieves medicines with their prescription counts.
        Given a lower weight (1) as it may be used less frequently for analytics.
        """
        self.client.get("/medicines/prescription-counts")