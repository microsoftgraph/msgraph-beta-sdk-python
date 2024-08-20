from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class RetrieveAssignedApplicationsReportPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The filter property
    filter: Optional[str] = None
    # The groupby property
    groupby: Optional[str] = None
    # The orderby property
    orderby: Optional[str] = None
    # The search property
    search: Optional[str] = None
    # The select property
    select: Optional[str] = None
    # The skip property
    skip: Optional[int] = None
    # The top property
    top: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RetrieveAssignedApplicationsReportPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RetrieveAssignedApplicationsReportPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RetrieveAssignedApplicationsReportPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "filter": lambda n : setattr(self, 'filter', n.get_str_value()),
            "groupby": lambda n : setattr(self, 'groupby', n.get_str_value()),
            "orderby": lambda n : setattr(self, 'orderby', n.get_str_value()),
            "search": lambda n : setattr(self, 'search', n.get_str_value()),
            "select": lambda n : setattr(self, 'select', n.get_str_value()),
            "skip": lambda n : setattr(self, 'skip', n.get_int_value()),
            "top": lambda n : setattr(self, 'top', n.get_int_value()),
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
        writer.write_str_value("filter", self.filter)
        writer.write_str_value("groupby", self.groupby)
        writer.write_str_value("orderby", self.orderby)
        writer.write_str_value("search", self.search)
        writer.write_str_value("select", self.select)
        writer.write_int_value("skip", self.skip)
        writer.write_int_value("top", self.top)
        writer.write_additional_data_value(self.additional_data)
    

