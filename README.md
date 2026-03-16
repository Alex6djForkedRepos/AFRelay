# AFRelay: Billing Microservice with integration to the Argentine Tax Agency

<p align="center">
  <img src="https://github.com/NehuenLian/AFRelay/actions/workflows/tests.yml/badge.svg" alt="CI">
  <img src="https://img.shields.io/codecov/c/github/NehuenLian/AFRelay?label=coverage&token=20WL0URAGI" alt="coverage">
  <img src="https://img.shields.io/github/license/NehuenLian/AFRelay" alt="License">
  <img src="https://img.shields.io/github/issues/NehuenLian/AFRelay" alt="Issues">
</p>

<p align="center">
  <a href="https://af-relay-docs.vercel.app/intro">Documentation</a>
  ·
  <a href="https://github.com/NehuenLian/AFRelay-E2E-Manual-tests">E2E tests repo</a>
</p>


**AFRelay** is a middleware that eliminates the need to manually build XML and lets developers work with AFIP as if it were a REST API.  
**Total control**: Free. No SaaS. No closed-source infrastructure.  
Without requiring the developer to get involved with SOAP.

- Async network I/O keeps the event loop free while waiting for slow external services.
- Automatically renews the access ticket each 11 hours and when the service starts.
- Does not automatically handle errors or raise exceptions, only returns information as JSON.

### Requirements

To use this service, you need a fiscal key and the corresponding certificates to authenticate with AFIP/ARCA web services.  
The steps to obtain the certificates are available on the official website:
https://www.arca.gob.ar/ws/documentacion/certificados.asp

Once authenticated, the authentication web service will provide two credentials:

- A private key with the extension "```.key```"
- An X.509 certificate with the extension "```.pem```"

They are used to sign the `loginTicketResponse.xml` file (TA), which returns an access token for the WSFE (Electronic Invoicing Web Service).
Once the necessary files have been obtained, they can be placed in the following directories depending on your infrastructure:
* `host_certs/`: For Docker environments.
* `src/shared/app_certs/`: For non-Docker setups.

### Quick start with Docker

1. Clone the repository
  ```bash
  git clone https://github.com/NehuenLian/AFRelay
  ```
2. Go to repository
  ```bash
  cd AFRelay
  ```
3. Start the container
  ```bash
  docker compose up
  ```
4. Health Check liveness:
  ```bash
  curl -i http://localhost:8000/health/liveness
  ```
5. See OpenAPI docs
  ```bash
  http://localhost:8000/docs
  ```

---

### Quick start without Docker

1. Clone the repository
  ```bash
  git clone https://github.com/NehuenLian/AFRelay
  ```
2. Go to repository
  ```bash
  cd AFRelay
  ```
3. Install dependencies
  ```bash
  pip install -r requirements-dev.txt
  ```
4. Startup FastAPI
  ```bash
  uvicorn src.shared.main:app --reload
  ```
5. Health Check liveness:
  ```bash
  curl -i http://127.0.0.1:8000/health/liveness
  ```
6. See OpenAPI docs
  ```bash
  http://localhost:8000/docs
  ```

### Run tests and see coverage

- Full tests:
  ```bash
  pytest -v --cov
  ```

### Additional Considerations

- **Access ticket persistence:**
  If the container or server where the service is deployed goes down, there is no problem with access tickets (`loginTicketResponse.xml`). On restart, if a TA (Access Ticket) comes in and the files are missing, the service will detect it and automatically generate a new ticket.

- **Flexible deployment:**
  Using Docker is optional. The service can run directly or inside any Python environment, as long as input and output file formats are respected. Protecting credentials (tokens, certificates) is the responsibility of the user or system administrator.

### Architecture

  ```text
  AFRelay/
  ├── .github/
  ├── docs/
  ├── host_certs/
  ├── host_xml/
  ├── src/
  │   ├── shared/
  │   ├── wsaa/
  │   └── wsfev1/
  ├── tests/
  ├── requirements-dev.txt
  └── requirements.txt
  ```

## License

This project is licensed under the [MIT](./LICENSE) license (a permissive open-source license).

You are free to use, copy, modify, and distribute the software, always including the copyright notice and without any warranties.

---

Author: Nehuen Lián https://github.com/NehuenLian