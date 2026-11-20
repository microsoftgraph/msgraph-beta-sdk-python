from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.request_http_method import RequestHttpMethod

@dataclass
class EvaluateAssignedPoliciesPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The includeNormalizedRequestInput property
    include_normalized_request_input: Optional[bool] = False
    # The isResultDetailed property
    is_result_detailed: Optional[bool] = False
    # The httpMethod property
    http_method: Optional[RequestHttpMethod] = None
    # The resourceUri property
    resource_uri: Optional[str] = None
    # The scope property
    scope: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EvaluateAssignedPoliciesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EvaluateAssignedPoliciesPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EvaluateAssignedPoliciesPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ....models.request_http_method import RequestHttpMethod

        from ....models.request_http_method import RequestHttpMethod

        fields: dict[str, Callable[[Any], None]] = {
            "httpMethod": lambda n : setattr(self, 'http_method', n.get_enum_value(RequestHttpMethod)),
            "includeNormalizedRequestInput": lambda n : setattr(self, 'include_normalized_request_input', n.get_bool_value()),
            "isResultDetailed": lambda n : setattr(self, 'is_result_detailed', n.get_bool_value()),
            "resourceUri": lambda n : setattr(self, 'resource_uri', n.get_str_value()),
            "scope": lambda n : setattr(self, 'scope', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("httpMethod", self.http_method)
        writer.write_bool_value("includeNormalizedRequestInput", self.include_normalized_request_input)
        writer.write_bool_value("isResultDetailed", self.is_result_detailed)
        writer.write_str_value("resourceUri", self.resource_uri)
        writer.write_str_value("scope", self.scope)
        writer.write_additional_data_value(self.additional_data)
    

