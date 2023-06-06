from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import email_identity, entity, payload_brand, payload_complexity, payload_delivery_platform, payload_detail, payload_industry, payload_theme, simulation_attack_technique, simulation_attack_type, simulation_content_source, simulation_content_status

from . import entity

@dataclass
class Payload(entity.Entity):
    # The branch of a payload. Possible values are: unknown, other, americanExpress, capitalOne, dhl, docuSign, dropbox, facebook, firstAmerican, microsoft, netflix, scotiabank, stewartTitle, tesco, wellsFargo, syrinxCloud, adobe, teams, zoom, unknownFutureValue.
    brand: Optional[payload_brand.PayloadBrand] = None
    # The complexity of a payload.Possible values are: unknown, low, medium, high, unknownFutureValue
    complexity: Optional[payload_complexity.PayloadComplexity] = None
    # Identity of the user who created the attack simulation and training campaign payload.
    created_by: Optional[email_identity.EmailIdentity] = None
    # Date and time when the attack simulation and training campaign payload.
    created_date_time: Optional[datetime] = None
    # Description of the attack simulation and training campaign payload.
    description: Optional[str] = None
    # Additional details about the payload.
    detail: Optional[payload_detail.PayloadDetail] = None
    # Display name of the attack simulation and training campaign payload. Supports $filter and $orderby.
    display_name: Optional[str] = None
    # Industry of a payload. Possible values are: unknown, other, banking, businessServices, consumerServices, education, energy, construction, consulting, financialServices, government, hospitality, insurance, legal, courierServices, IT, healthcare, manufacturing, retail, telecom, realEstate, unknownFutureValue.
    industry: Optional[payload_industry.PayloadIndustry] = None
    # Indicates whether the attack simulation and training campaign payload was created from an automation flow. Supports $filter and $orderby.
    is_automated: Optional[bool] = None
    # Indicates whether the payload is controversial.
    is_controversial: Optional[bool] = None
    # Indicates whether the payload is from any recent event.
    is_current_event: Optional[bool] = None
    # Payload language.
    language: Optional[str] = None
    # Identity of the user who most recently modified the attack simulation and training campaign payload.
    last_modified_by: Optional[email_identity.EmailIdentity] = None
    # Date and time when the attack simulation and training campaign payload was last modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Free text tags for a payload.
    payload_tags: Optional[List[str]] = None
    # The payload delivery platform for a simulation. Possible values are: unknown, sms, email, teams, unknownFutureValue.
    platform: Optional[payload_delivery_platform.PayloadDeliveryPlatform] = None
    # Predicted probability for a payload to phish a targeted user.
    predicted_compromise_rate: Optional[float] = None
    # Attack type of the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, social, cloud, endpoint, unknownFutureValue.
    simulation_attack_type: Optional[simulation_attack_type.SimulationAttackType] = None
    # The source property
    source: Optional[simulation_content_source.SimulationContentSource] = None
    # Simulation content status. Supports $filter and $orderby. Possible values are: unknown, draft, ready, archive, delete, unknownFutureValue. Inherited from simulation.
    status: Optional[simulation_content_status.SimulationContentStatus] = None
    # The social engineering technique used in the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, credentialHarvesting, attachmentMalware, driveByUrl, linkInAttachment, linkToMalwareFile, unknownFutureValue. For more information on the types of social engineering attack techniques, see simulations.
    technique: Optional[simulation_attack_technique.SimulationAttackTechnique] = None
    # The theme of a payload. Possible values are: unknown, other, accountActivation, accountVerification, billing, cleanUpMail, controversial, documentReceived, expense, incomingMessages, invoice, itemReceived, loginAlert, mailReceived, password, payment, payroll, personalizedOffer, quarantine, remoteWork, reviewMessage, securityUpdate, serviceSuspended, signatureRequired, upgradeMailboxStorage, verifyMailbox, voicemail, advertisement, employeeEngagement, unknownFutureValue.
    theme: Optional[payload_theme.PayloadTheme] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Payload:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Payload
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Payload()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import email_identity, entity, payload_brand, payload_complexity, payload_delivery_platform, payload_detail, payload_industry, payload_theme, simulation_attack_technique, simulation_attack_type, simulation_content_source, simulation_content_status

        fields: Dict[str, Callable[[Any], None]] = {
            "brand": lambda n : setattr(self, 'brand', n.get_enum_value(payload_brand.PayloadBrand)),
            "complexity": lambda n : setattr(self, 'complexity', n.get_enum_value(payload_complexity.PayloadComplexity)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(email_identity.EmailIdentity)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "detail": lambda n : setattr(self, 'detail', n.get_object_value(payload_detail.PayloadDetail)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "industry": lambda n : setattr(self, 'industry', n.get_enum_value(payload_industry.PayloadIndustry)),
            "isAutomated": lambda n : setattr(self, 'is_automated', n.get_bool_value()),
            "isControversial": lambda n : setattr(self, 'is_controversial', n.get_bool_value()),
            "isCurrentEvent": lambda n : setattr(self, 'is_current_event', n.get_bool_value()),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(email_identity.EmailIdentity)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "payloadTags": lambda n : setattr(self, 'payload_tags', n.get_collection_of_primitive_values(str)),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(payload_delivery_platform.PayloadDeliveryPlatform)),
            "predictedCompromiseRate": lambda n : setattr(self, 'predicted_compromise_rate', n.get_float_value()),
            "simulationAttackType": lambda n : setattr(self, 'simulation_attack_type', n.get_enum_value(simulation_attack_type.SimulationAttackType)),
            "source": lambda n : setattr(self, 'source', n.get_enum_value(simulation_content_source.SimulationContentSource)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(simulation_content_status.SimulationContentStatus)),
            "technique": lambda n : setattr(self, 'technique', n.get_enum_value(simulation_attack_technique.SimulationAttackTechnique)),
            "theme": lambda n : setattr(self, 'theme', n.get_enum_value(payload_theme.PayloadTheme)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("brand", self.brand)
        writer.write_enum_value("complexity", self.complexity)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_object_value("detail", self.detail)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("industry", self.industry)
        writer.write_bool_value("isAutomated", self.is_automated)
        writer.write_bool_value("isControversial", self.is_controversial)
        writer.write_bool_value("isCurrentEvent", self.is_current_event)
        writer.write_str_value("language", self.language)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_primitive_values("payloadTags", self.payload_tags)
        writer.write_enum_value("platform", self.platform)
        writer.write_float_value("predictedCompromiseRate", self.predicted_compromise_rate)
        writer.write_enum_value("simulationAttackType", self.simulation_attack_type)
        writer.write_enum_value("source", self.source)
        writer.write_enum_value("status", self.status)
        writer.write_enum_value("technique", self.technique)
        writer.write_enum_value("theme", self.theme)
    

