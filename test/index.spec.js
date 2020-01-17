import puppeteer from "puppeteer";

const localUrlBase = "http://127.0.0.1:8080";
const routes = {
    public: {
        register: `${localUrlBase}/register_page`,
        login: `${localUrlBase}/login`
    },
    user: {
        userPage: `${localUrlBase}/orders_display_users`,
        singleOrderPage: `${localUrlBase}/order_display_page`
    },
    admin: {
        adminPage: `${localUrlBase}/orders_display_admin`
    }
};
const user = {
    email: "paul@hotmail.com",
    emailFail: "paulhotmail.com",
    password: "Tykenyke",
    passwordFail: "tykenyke"
};
const admin = {
    email: "Davidtroy@sendIT.org",
    password: "Tykenyke"
};
const parcel = {
    name: "Twenty Heifer Skins",
    pickup: "Kisumu",
    dest: "Turkwell",
    price: "6000"
};
const dummyParcel = {
    name: " ",
    pickup: " ",
    dest: " ",
    price: " "
};
let browser;
let page;

beforeAll(async () => {
    browser = await puppeteer.launch();
    page = await browser.newPage();
});

describe("Registration", () => {
    test("generation of response", async () => {
        await page.goto(routes.public.register);
        await page.waitForSelector('[data-testid="registerForm"]');
        await page.click('[data-testid="emailInput"]');
        await page.type('[data-testid="emailInput"]', user.email);
        await page.click('[data-testid="passwordInput"]');
        await page.type('[data-testid="passwordInput"]', user.password);
        await page.click('[data-testid="registerSubmitButton"]');
        await page.waitForSelector('[data-testid="responseBox"]');
    });
    test("duplicate email response message", async () => {
        await page.type('[data-testid="emailInput"]', user.emailFail);
        await page.click('[data-testid="passwordInput"]');
        await page.type('[data-testid="passwordInput"]', user.passwordFail);
        await page.click('[data-testid="registerSubmitButton"]');
        await page.waitForSelector('[data-testid="responseBox"]');
        const duplicateEmail = await page.$eval('[data-testid="responseBox"]', el => el.textContent);
        expect(duplicateEmail).toEqual("User with the email already exists");
    });
    test("wrong email format message", async () => {
        await page.goto(routes.public.register);
        await page.waitForSelector('[data-testid="registerForm"]');
        await page.click('[data-testid="emailInput"]');
        await page.type('[data-testid="emailInput"]', user.emailFail);
        await page.click('[data-testid="passwordInput"]');
        await page.type('[data-testid="passwordInput"]', user.password);
        await page.click('[data-testid="registerSubmitButton"]');
        await page.waitForSelector('[data-testid="responseBox"]');
        const wrongEmailFormat = await page.$eval('[data-testid="responseBox"]', el => el.textContent);
        expect(wrongEmailFormat).toEqual("Invalid email format");
    });
});

describe("Login", () => {
    test("throws error message for invalid email format", async () => {
        await page.goto(routes.public.login);
        await page.waitForSelector('[data-testid="logInForm"]');
        await page.click('[data-testid="logInEmailInput"]');
        await page.type('[data-testid="logInEmailInput"]', user.emailFail);
        await page.click('[data-testid="logInPasswordInput"]');
        await page.type('[data-testid="logInPasswordInput"]', user.password);
        await page.click('[data-testid="loginSubmitButton"]');
        await page.waitForSelector('[data-testid="logInResponseBox"]');
        const errorMessage = await page.$eval('[data-testid="logInResponseBox"]', el => el.textContent);
        expect(errorMessage).toEqual("Invalid email. please check the format");
    });
    test("throws error message for wrong login credentials", async () => {
        await page.goto(routes.public.login);
        await page.waitForSelector('[data-testid="logInForm"]');
        await page.click('[data-testid="logInEmailInput"]');
        await page.type('[data-testid="logInEmailInput"]', user.email);
        await page.click('[data-testid="logInPasswordInput"]');
        await page.type('[data-testid="logInPasswordInput"]', "  ");
        await page.click('[data-testid="loginSubmitButton"]');
        await page.waitForSelector('[data-testid="logInResponseBox"]');
        const errorMessage = await page.$eval('[data-testid="logInResponseBox"]', el => el.textContent);
        expect(errorMessage).toEqual("incorrect login credentials. please enter details again");
    });
    test("successful login triggers a redirect to user account", async () => {
        await page.goto(routes.public.login);
        await page.waitForSelector('[data-testid="logInForm"]');
        await page.click('[data-testid="logInEmailInput"]');
        await page.type('[data-testid="logInEmailInput"]', user.email);
        await page.click('[data-testid="logInPasswordInput"]');
        await page.type('[data-testid="logInPasswordInput"]', user.password);
        await page.click('[data-testid="loginSubmitButton"]');
        await page.waitForNavigation({waitUntil: "networkidle2"});
        await page.waitForSelector('[data-testid="logInRedirectResponse"]');
        const duplicateEmail = await page.$eval('[data-testid="logInRedirectResponse"]', el => el.textContent);
        expect(duplicateEmail).toEqual("Successfully logged in");  
    });
    test("successful login triggers a redirect to admin account", async () => {
        await page.goto(routes.public.login);
        await page.waitForSelector('[data-testid="logInForm"]');
        await page.click('[data-testid="logInEmailInput"]');
        await page.type('[data-testid="logInEmailInput"]', admin.email);
        await page.click('[data-testid="logInPasswordInput"]');
        await page.type('[data-testid="logInPasswordInput"]', admin.password);
        await page.click('[data-testid="loginSubmitButton"]');
        await page.waitForNavigation({waitUntil: "networkidle2"});
        await page.waitForSelector('[data-testid="allOrdersAdmin"]');
        const duplicateEmail = await page.$eval('[data-testid="allOrdersAdmin"]', el => el.textContent);
        expect(duplicateEmail).toEqual("View all Orders");  
    });
});

describe("User dashboard", () => {
    test("assert user can view all orders they make", async () => {
        await page.goto(routes.public.login);
        await page.waitForSelector('[data-testid="logInForm"]');
        await page.click('[data-testid="logInEmailInput"]');
        await page.type('[data-testid="logInEmailInput"]', user.email);
        await page.click('[data-testid="logInPasswordInput"]');
        await page.type('[data-testid="logInPasswordInput"]', user.password);
        await page.click('[data-testid="loginSubmitButton"]');
        await page.waitForNavigation({waitUntil: "networkidle2"});
        await page.waitForSelector('[data-testid="viewUserOrderButton"]');
        await page.click('[data-testid="viewUserOrderButton"]');
        await page.waitForSelector('[data-testid="generatedUserOrders"]');        
    });
    test("assert user can submit delivery order fields", async () => {
        await page.waitForSelector('[data-testid="parcelCreationForm"]');
        await page.click('[data-testid="orderNameInput"]');
        await page.type('[data-testid="orderNameInput"]', dummyParcel.name);
        await page.click('[data-testid="orderPickUpInput"]');
        await page.type('[data-testid="orderPickUpInput"]', parcel.pickup);
        await page.click('[data-testid="orderDestInput"]');
        await page.type('[data-testid="orderDestInput"]', parcel.dest);
        await page.click('[data-testid="orderPriceInput"]');
        await page.type('[data-testid="orderPriceInput"]', parcel.price);
        await page.click('[data-testid="createParcelSubmitButton"]');
        await page.waitForSelector('[data-testid="createOrderFailResponse"]');
    });
    test("assert user can redirect to single order info page", async () => {
        await page.waitForSelector('[data-testid="generatedUserOrders"]');
        await page.click('[data-testid="generatedUserOrders"]');
        await page.waitForNavigation({waitUntil: "networkidle2"});
        await page.waitForSelector('[data-testid="singleOrderPage"]');    
    });
    test("assert user can retrieve an order by id", async () => {
        await page.waitForSelector('[data-testid="singleOrderForm"]');
        await page.click('[data-testid="orderIdInput"]');
        await page.type('[data-testid="orderIdInput"]', "3");
        await page.click('[data-testid="viewOrderInfo"]');
        await page.waitForSelector('[data-testid="returnedOrder"]');
        const orderHeading = await page.$eval('[data-testid="returnedOrder"]', el => el.textContent);
        expect(orderHeading).toEqual("Three Harry Potter Books"); 
    });
    test("assert user can update order destination", async () => {
        await page.waitForSelector('[data-testid="singleOrderForm"]');
        await page.click('[data-testid="updateOrderDestination"]');
        await page.type('[data-testid="updateOrderDestination"]', "Nakuru");
        await page.click('[data-testid="submitNewDestination"]');
        await page.waitForSelector('[data-testid="updatedDestination"]');
        const updatedOrderDestination = await page.$eval('[data-testid="updatedDestination"]', el => el.textContent);
        expect(updatedOrderDestination).toEqual("New destination updated"); 
    });
    test("assert user can cancel order", async () => {
        await page.waitForSelector('[data-testid="singleOrderForm"]');
        await page.click('[data-testid="cancelOrder"]');
        await page.waitForSelector('[data-testid="cancelResponse"]');
        const cancelOrderResponse = await page.$eval('[data-testid="cancelResponse"]', el => el.textContent);
        expect(cancelOrderResponse).toEqual("order is cancelled"); 
    });
});

describe("Admin dashboard", () => {
    test("assert admin can view all orders made by all users", async () => {
        await page.goto(routes.public.login);
        await page.waitForSelector('[data-testid="logInForm"]');
        await page.click('[data-testid="logInEmailInput"]');
        await page.type('[data-testid="logInEmailInput"]', admin.email);
        await page.click('[data-testid="logInPasswordInput"]');
        await page.type('[data-testid="logInPasswordInput"]', admin.password);
        await page.click('[data-testid="loginSubmitButton"]');
        await page.waitForNavigation({waitUntil: "networkidle2"});
        await page.waitForSelector('[data-testid="allOrdersAdmin"]');
        await page.click('[data-testid="allOrdersAdmin"]');
        await page.waitForSelector('[data-testid="generatedAllOrders"]');        
    });
    test("assert admin can update the current location of a parcel", async () => {
        await page.waitForSelector('[data-testid="updateLocationForm"]');
        await page.click('[data-testid="parcelIdInput"]');
        await page.type('[data-testid="parcelIdInput"]', "1");
        await page.click('[data-testid="parcelLocationInput"]');
        await page.type('[data-testid="parcelLocationInput"]', "Homabay");
        await page.click('[data-testid="updateLocationButton"]');
        await page.waitForSelector('[data-testid="updateLocationResponse"]');
    });
    test("assert admin can update status of a parcel", async () => {
        await page.waitForSelector('[data-testid="updateOrderStatus"]');
        await page.click('[data-testid="updateOrderStatus"]');
        await page.type('[data-testid="updateOrderStatus"]', "Arrived");
        await page.click('[data-testid="orderStatusButton"]');
        await page.waitForSelector('[data-testid="orderStatusResponse"]');    
    });
});

/*
describe('User parcel creation', () => {
    
    test('assert user can view all orders they make', async () => {
        await page.goto(routes.public.login)
        await page.waitForSelector('[data-testid="logInForm"]')
        await page.click('[data-testid="logInEmailInput"]')
        await page.type('[data-testid="logInEmailInput"]', user.email)
        await page.click('[data-testid="logInPasswordInput"]')
        await page.type('[data-testid="logInPasswordInput"]', user.password)
        await page.click('[data-testid="loginSubmitButton"]')
        await page.waitForNavigation({waitUntil: "networkidle2"})
        await page.waitForSelector('[data-testid="parcelCreationForm"]')
        await page.click('[data-testid="orderNameInput"]')
        await page.type('[data-testid="orderNameInput"]', dummyParcel.name)
        await page.click('[data-testid="orderPickUpInput"]')
        await page.type('[data-testid="orderPickUpInput"]', parcel.pickup)
        await page.click('[data-testid="orderDestInput"]')
        await page.type('[data-testid="orderDestInput"]', parcel.dest)
        await page.click('[data-testid="orderPriceInput"]')
        await page.type('[data-testid="orderPriceInput"]', parcel.price)
        await page.click('[data-testid="createParcelSubmitButton"]')
        await page.waitForSelector('[data-testid="redirectedLogIn"]')
        expect.assertions(1)
        const invalidParcelName = await page.$eval('[data-testid="redirectedLogIn"]', el => el.textContent)
        return expect(invalidParcelName).toEqual("Invalid item name format")       
    });
}); */

afterAll(async (done) => {
    browser.close();
    done();
});
