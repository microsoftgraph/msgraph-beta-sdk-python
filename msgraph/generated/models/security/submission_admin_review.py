from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .submission_result_category import SubmissionResultCategory

@dataclass
class SubmissionAdminReview(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies who reviewed the email. The identification is an email ID or other identity strings.
    review_by: Optional[str] = None
    # Specifies the date time when the review occurred.
    review_date_time: Optional[datetime.datetime] = None
    # Specifies what the review result was. The possible values are: notJunk, spam, phishing, malware, allowedByPolicy, blockedByPolicy, spoof, unknown, noResultAvailable, and unknownFutureValue.
    review_result: Optional[SubmissionResultCategory] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SubmissionAdminReview:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SubmissionAdminReview
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SubmissionAdminReview()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .submission_result_category import SubmissionResultCategory

        from .submission_result_category import SubmissionResultCategory

        fields: Dict[str, Callable[[Any], None]] = {
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reviewBy": lambda n : setattr(self, 'review_by', n.get_str_value()),
            "reviewDateTime": lambda n : setattr(self, 'review_date_time', n.get_datetime_value()),
            "reviewResult": lambda n : setattr(self, 'review_result', n.get_enum_value(SubmissionResultCategory)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("reviewBy", self.review_by)
        writer.write_datetime_value("reviewDateTime", self.review_date_time)
        writer.write_enum_value("reviewResult", self.review_result)
        writer.write_additional_data_value(self.additional_data)
    

