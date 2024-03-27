operation_parameter_map = {
    '/v2/payments/authorizations/{authorization_id}/capture-POST': {
        'parameters': [
            {
                'name': 'authorization_id'
            },
            {
                'name': 'invoice_id'
            },
            {
                'name': 'note_to_payer'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'final_capture'
            },
            {
                'name': 'payment_instruction'
            },
            {
                'name': 'soft_descriptor'
            },
            {
                'name': 'PayPal-Request-Id'
            },
            {
                'name': 'Prefer'
            },
        ]
    },
    '/v2/payments/authorizations/{authorization_id}/reauthorize-POST': {
        'parameters': [
            {
                'name': 'authorization_id'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'PayPal-Request-Id'
            },
            {
                'name': 'Prefer'
            },
        ]
    },
    '/v2/payments/authorizations/{authorization_id}-GET': {
        'parameters': [
            {
                'name': 'authorization_id'
            },
        ]
    },
    '/v2/payments/authorizations/{authorization_id}/void-POST': {
        'parameters': [
            {
                'name': 'authorization_id'
            },
            {
                'name': 'PayPal-Auth-Assertion'
            },
            {
                'name': 'Prefer'
            },
        ]
    },
    '/v2/payments/captures/{capture_id}/refund-POST': {
        'parameters': [
            {
                'name': 'capture_id'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'custom_id'
            },
            {
                'name': 'invoice_id'
            },
            {
                'name': 'note_to_payer'
            },
            {
                'name': 'payment_instruction'
            },
            {
                'name': 'PayPal-Request-Id'
            },
            {
                'name': 'Prefer'
            },
            {
                'name': 'PayPal-Auth-Assertion'
            },
        ]
    },
    '/v2/payments/captures/{capture_id}-GET': {
        'parameters': [
            {
                'name': 'capture_id'
            },
        ]
    },
    '/v2/payments/refunds/{refund_id}-GET': {
        'parameters': [
            {
                'name': 'refund_id'
            },
        ]
    },
};