from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .policies_evaluation_detail import PoliciesEvaluationDetail
    from .policy_effects import PolicyEffects
    from .request_http_method import RequestHttpMethod

@dataclass
class PoliciesEvaluationResult(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The appliedPoliciesEffects property
    applied_policies_effects: Optional[PolicyEffects] = None
    # The details property
    details: Optional[list[PoliciesEvaluationDetail]] = None
    # The httpMethod property
    http_method: Optional[RequestHttpMethod] = None
    # The isBlocked property
    is_blocked: Optional[bool] = None
    # The message property
    message: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The resourceUri property
    resource_uri: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PoliciesEvaluationResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PoliciesEvaluationResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PoliciesEvaluationResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .policies_evaluation_detail import PoliciesEvaluationDetail
        from .policy_effects import PolicyEffects
        from .request_http_method import RequestHttpMethod

        from .policies_evaluation_detail import PoliciesEvaluationDetail
        from .policy_effects import PolicyEffects
        from .request_http_method import RequestHttpMethod

        fields: dict[str, Callable[[Any], None]] = {
            "appliedPoliciesEffects": lambda n : setattr(self, 'applied_policies_effects', n.get_collection_of_enum_values(PolicyEffects)),
            "details": lambda n : setattr(self, 'details', n.get_collection_of_object_values(PoliciesEvaluationDetail)),
            "httpMethod": lambda n : setattr(self, 'http_method', n.get_enum_value(RequestHttpMethod)),
            "isBlocked": lambda n : setattr(self, 'is_blocked', n.get_bool_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resourceUri": lambda n : setattr(self, 'resource_uri', n.get_str_value()),
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
        writer.write_enum_value("appliedPoliciesEffects", self.applied_policies_effects)
        writer.write_enum_value("httpMethod", self.http_method)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

