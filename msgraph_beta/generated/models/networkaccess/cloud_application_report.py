from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .traffic_type import TrafficType

@dataclass
class CloudApplicationReport(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The list of categories for the application. Supported values are: Collaboration, Business Management, Consumer, Content management, CRM, Data services, Developer services, E-commerce, Education, ERP, Finance, Health, Human resources, IT infrastructure, Mail, Management, Marketing, Media, Productivity, Project management, Telecommunications, Tools, Travel, and Web design & hosting.
    categories: Optional[list[str]] = None
    # The ID of the application in the SaaS application catalog.
    cloud_application_catalog_id: Optional[str] = None
    # The compliance score of the application.
    compliance_score: Optional[int] = None
    # Number of devices under this application.
    device_count: Optional[int] = None
    # Timestamp of the first access to the application.
    first_access_date_time: Optional[datetime.datetime] = None
    # The general score of the application.
    general_score: Optional[int] = None
    # Timestamp of the last access to the application.
    last_access_date_time: Optional[datetime.datetime] = None
    # The legal score of the application.
    legal_score: Optional[int] = None
    # The name of the application (e.g., ChatGPT, Salesforce, Bing).
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The risk score of the application.
    risk_score: Optional[int] = None
    # The security score of the application.
    security_score: Optional[int] = None
    # Total bytes received from the application.
    total_bytes_received: Optional[int] = None
    # Total bytes sent to the application.
    total_bytes_sent: Optional[int] = None
    # The trafficType property
    traffic_type: Optional[TrafficType] = None
    # Number of transactions under this application.
    transaction_count: Optional[int] = None
    # Number of users under this application.
    user_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudApplicationReport:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudApplicationReport
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudApplicationReport()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .traffic_type import TrafficType

        from .traffic_type import TrafficType

        fields: dict[str, Callable[[Any], None]] = {
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(str)),
            "cloudApplicationCatalogId": lambda n : setattr(self, 'cloud_application_catalog_id', n.get_str_value()),
            "complianceScore": lambda n : setattr(self, 'compliance_score', n.get_int_value()),
            "deviceCount": lambda n : setattr(self, 'device_count', n.get_int_value()),
            "firstAccessDateTime": lambda n : setattr(self, 'first_access_date_time', n.get_datetime_value()),
            "generalScore": lambda n : setattr(self, 'general_score', n.get_int_value()),
            "lastAccessDateTime": lambda n : setattr(self, 'last_access_date_time', n.get_datetime_value()),
            "legalScore": lambda n : setattr(self, 'legal_score', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "riskScore": lambda n : setattr(self, 'risk_score', n.get_int_value()),
            "securityScore": lambda n : setattr(self, 'security_score', n.get_int_value()),
            "totalBytesReceived": lambda n : setattr(self, 'total_bytes_received', n.get_int_value()),
            "totalBytesSent": lambda n : setattr(self, 'total_bytes_sent', n.get_int_value()),
            "trafficType": lambda n : setattr(self, 'traffic_type', n.get_enum_value(TrafficType)),
            "transactionCount": lambda n : setattr(self, 'transaction_count', n.get_int_value()),
            "userCount": lambda n : setattr(self, 'user_count', n.get_int_value()),
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
        writer.write_collection_of_primitive_values("categories", self.categories)
        writer.write_str_value("cloudApplicationCatalogId", self.cloud_application_catalog_id)
        writer.write_int_value("complianceScore", self.compliance_score)
        writer.write_int_value("deviceCount", self.device_count)
        writer.write_datetime_value("firstAccessDateTime", self.first_access_date_time)
        writer.write_int_value("generalScore", self.general_score)
        writer.write_datetime_value("lastAccessDateTime", self.last_access_date_time)
        writer.write_int_value("legalScore", self.legal_score)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("riskScore", self.risk_score)
        writer.write_int_value("securityScore", self.security_score)
        writer.write_int_value("totalBytesReceived", self.total_bytes_received)
        writer.write_int_value("totalBytesSent", self.total_bytes_sent)
        writer.write_enum_value("trafficType", self.traffic_type)
        writer.write_int_value("transactionCount", self.transaction_count)
        writer.write_int_value("userCount", self.user_count)
        writer.write_additional_data_value(self.additional_data)
    

